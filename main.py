import csv
from eth_account import Account
from mnemonic import Mnemonic

def generate_eth_wallets(num_wallets, csv_filename):
    # 启用加密功能（必须调用）
    Account.enable_unaudited_hdwallet_features()

    # 打开 CSV 文件准备写入，指定编码为 utf-8-sig
    with open(csv_filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(["序号", "助记词", "私钥", "地址"])

        for i in range(num_wallets):
            # 生成助记词
            mnemo = Mnemonic("english")
            mnemonic_phrase = mnemo.generate(strength=128)  # 12个单词的助记词

            # 从助记词生成钱包
            account = Account.from_mnemonic(mnemonic_phrase)

            # 写入 CSV 文件
            writer.writerow([
                i + 1,  # 序号
                mnemonic_phrase,  # 助记词
                account.key.hex(),  # 私钥
                account.address  # 地址
            ])

            # 打印到控制台（可选）
            print(f"\n=== 钱包 {i+1} ===")
            print("助记词:", mnemonic_phrase)
            print("私钥:  ", account.key.hex())
            print("地址:  ", account.address)
            print("=" * 20)

    print(f"\n钱包信息已保存到文件: {csv_filename}")

if __name__ == "__main__":
    try:
        num = int(input("请输入要生成的钱包数量: "))
        if num <= 0:
            raise ValueError("数量必须大于0")
        
        # 定义 CSV 文件名
        csv_filename = "eth_wallets.csv"
        generate_eth_wallets(num, csv_filename)
    except ValueError as e:
        print(f"错误: {e}")
