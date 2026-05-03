{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f089485b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a positive integer N: 9\n"
     ]
    }
   ],
   "source": [
    "N = int(input('Enter a positive integer N: '))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "2ce44d69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number 1: 1\n",
      "Enter number 2: 3\n",
      "Enter number 3: 9\n",
      "Enter number 4: 12\n",
      "Enter number 5: 15\n",
      "Enter number 6: 15\n",
      "Enter number 7: 15\n",
      "Enter number 8: 7\n",
      "Enter number 9: 15\n"
     ]
    }
   ],
   "source": [
    "numbers = []\n",
    "for i in range(1, N+1):\n",
    "    user_num = int(input(f'Enter number {i}: '))\n",
    "    numbers.append(user_num)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "7aaf2d0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter the integer X: 15\n"
     ]
    }
   ],
   "source": [
    "X = int(input('Please enter the integer X: '))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "3b1384a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found at index: 5\n",
      "Found at index: 6\n",
      "Found at index: 7\n",
      "Found at index: 9\n"
     ]
    }
   ],
   "source": [
    "found = False\n",
    "for i in range(N):\n",
    "    if numbers[i] == X:\n",
    "        print(f\"Found at index: {i + 1}\")  # convert to 1-based index\n",
    "        found = True\n",
    "        \n",
    "if not found:\n",
    "    print(-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21574fc1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ab20a3b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10 (yfinance)",
   "language": "python",
   "name": "yf310"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
