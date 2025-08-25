'''
@Project  ：pytest-solidity-api 
@File     ：transfer_test
@Author   ：le
@Date     ：2025/8/19 17:41
'''

from datetime import datetime, timedelta
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

import requests
import schedule
from dotenv import load_dotenv
from eth_account.messages import encode_defunct
from common.rpc_account import RpcConnect

def transfer_test(index, key, amount, max_retries=5):
    account = RpcConnect().account(web3, key=key)
    retry_count = 0  # 失败重试计数

    while retry_count < max_retries:
        try:
            random_amount = amount + random.uniform(0.01, 0.05)
            amount_in_wei = web3.to_wei(random_amount, "ether")
            # print(f"[{index}]|开始执行任务 (尝试 {retry_count + 1}/{max_retries})")

            gas_price = web3.eth.gas_price
            balance = web3.eth.get_balance(account.address)

            if web3.from_wei(balance, 'ether') > 0.001:
                # print(f"[{index}][{account.address}] 余额：{web3.from_wei(balance, 'ether')} XOC")

                transaction = {
                    'to': account.address,
                    'value': int(amount_in_wei),
                    'gas': 30000,
                    'gasPrice': gas_price,
                    'nonce': web3.eth.get_transaction_count(account.address),
                    'chainId': 33772211
                }

                signed_transaction = web3.eth.account.sign_transaction(transaction, key)
                tx_hash = web3.eth.send_raw_transaction(signed_transaction.raw_transaction)
                tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

                if tx_receipt["status"] == 1:
                    # print(web3.eth.get_transaction(tx_hash.hex())["blockNumber"])
                    blockNumber = web3.eth.get_transaction(tx_hash.hex())["blockNumber"]
                    print(f"[{index}][{account.address}] | ✅ | 转账成功 | hash: {tx_hash.hex()} | 区块高度 {blockNumber}")
                    return  # 成功后退出函数，不再重试
                else:
                    print(f"[{index}][{account.address}] | ❌ | 交易失败 : {tx_receipt}")

            else:
                print(f"[{index}][{account.address}] | ❌ | 余额不足 | 余额：{web3.from_wei(balance, 'ether')}")
                return  # 余额不足时直接退出，不重试

        except Exception as e:
            print(f"[{index}][{account.address}] | ❌ | 转账失败: {str(e)}")

        retry_count += 1
        if retry_count < max_retries:
            print(f"[{index}][{account.address}] | 🔄 | {retry_count} 次尝试失败，等待 5 秒后重试...")
            sleep(5)  # 失败后等待 5 秒再试
        else:
            print(f"[{index}][{account.address}] | ❌ | 转账失败，已达到最大重试次数")



def main():
    keys = RpcConnect().read_keys("key.csv", "key")
    rpc_url = "https://rpc-testnet.xone.plus"
    workers = 10  # 并发任务数
    amount = 0.01  # 转账金额

    global web3  # 声明全局变量
    max_rpc_retries = 2  # 最大 RPC 连接重试次数
    rpc_retry_count = 0

    while rpc_retry_count < max_rpc_retries:
        web3 = RpcConnect().connect_rpc(rpc_url)
        if web3 and web3.is_connected():
            break
        else:
            print(f"⚠️  RPC 连接失败，重试 {rpc_retry_count + 1}/{max_rpc_retries}...")
            rpc_retry_count += 1
            sleep(5)
    else:
        print("❌ 无法连接到 RPC 服务器，退出程序")
        return
    for x in range(200):
        print(f"执行第{x+1}轮")
        for i in range(0, len(keys), workers):
            batch_keys = keys[i:i + workers]

            # **执行 transfer_test 任务，失败会自动重试**
            with ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {executor.submit(transfer_test, index + i, key, amount): index for index, key in
                           enumerate(batch_keys)}
                for future in as_completed(futures):
                    future.result()  # 确保每个任务都执行完毕
            count = 0
            print(f"⏳ {workers} 个任务执行完毕，等待 {count} 秒后继续...")
            sleep(count)

    print("✅ 所有 transfer_test 任务完成")

if __name__ == '__main__':
    main()