
import numpy as np
import matplotlib.pyplot as plt

def binary_predict(number: int = 1) -> int:
    count = 0
    low = 1
    high = 100
    while True:
        count += 1
        predict = (low + high) // 2
        if predict == number:
            break
        elif predict < number:
            low = predict + 1
        else:
            high = predict - 1
    return count

def random_predict(number: int = 1) -> int:
    count = 0
    while True:
        count += 1
        if number == np.random.randint(1, 101):
            break
    return count

def score_game(predict_func, seed: int = 1):
    np.random.seed(seed)
    test_numbers = np.random.randint(1, 101, size=1000)
    attempts = [predict_func(number) for number in test_numbers]
    return attempts

if __name__ == '__main__':
    random_attempts = score_game(random_predict, seed=42)
    binary_attempts = score_game(binary_predict, seed=42)

    import pandas as pd
    df = pd.DataFrame({'Random': random_attempts, 'Binary': binary_attempts})

    print("Среднее количество попыток:")
    print(df.mean())

    plt.figure(figsize=(10, 6))
    plt.hist(random_attempts, bins=range(1, max(random_attempts)+2), alpha=0.6, label='Random')
    plt.hist(binary_attempts, bins=range(1, max(binary_attempts)+2), alpha=0.6, label='Binary Search')
    plt.title('Распределение количества попыток угадывания числа')
    plt.xlabel('Количество попыток')
    plt.ylabel('Частота')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("attempts_distribution.png")
