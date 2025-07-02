from fastapi import FastAPI

app = FastAPI()

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
 
def strong_number(num):
    digits = str(num)
    sum_factorials = sum(factorial(int(digit)) for digit in digits)
    if sum_factorials == num:
        return 'Strong Number'
    else:
        return 'Not a Strong Number'

@app.get('/check_strong/{num}')
def check_strong(num: int):
    return strong_number(num)   


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')