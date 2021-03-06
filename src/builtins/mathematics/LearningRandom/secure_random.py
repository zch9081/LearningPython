#!/usr/bin/env python
# encoding: utf-8

import random
import secrets

# 伪随机数。
# 产生的随机数可以是均匀分布，高斯分布，对数正态分布，负指数分布以及alpha，beta分布。
# 这些随机数都是伪随机数，不能应用于安全加密目的的应用中。
sr = random.randint(0, 100)
print("Fake random number generated by random: %s." % sr)

# 也是伪随机数。
# random 模块还提供 SystemRandom 类，
# 使用系统函数 os.urandom() 从操作系统提供的源生成随机数。
foo = random.SystemRandom()
print("Fake random number generated by SystemRandom: %s." % foo.random())
print("Fake random number generated by SystemRandom: %s." % foo.randint(0, 10))

# 在Python 3.6及更高版本中添加了secrets模块。
# 可以使用secrets模块来实现：生成安全随机数、密码及一次性密码、随机token及会话密钥等功能。
number = secrets.randbelow(10)
print("Secure random generated by secrets: ", number)

secretsGenerator = secrets.SystemRandom()
randomNumber = secretsGenerator.randint(0, 50)
print("Secure random number is ", randomNumber)
# Secure random number is 26

# 指定范围并设置步长
randomNumber = secretsGenerator.randrange(5, 50, 5)
print("Secure random number within range is ", randomNumber)
# Secure random number within range is 15

# 从指定的数据集中选择
number_list = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
secure_choice = secretsGenerator.choice(number_list)
print("Secure random choice using secrets is ", secure_choice)

# Secure random choice using secrets is 30
secure_sample = secretsGenerator.sample(number_list, 3)
print("Secure random sample using secrets is ", secure_sample)

# 随机安全浮点数
secure_float = secretsGenerator.uniform(2.5, 25.5)
print("Secure random float number using secrets is ", secure_float)

randLength = 16
with open("/dev/random", 'rb') as file:
    sr = file.read(randLength)
print("Secure random get from /dev/random: ", sr)
