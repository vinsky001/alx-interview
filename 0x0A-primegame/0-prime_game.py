#!/usr/bin/python3


def isWinner(x, nums):
    """
    Determines the winner of a game played by Maria and Ben.
    They take turns choosing a prime number from a set of consecutive \
    integers starting from 1 up to and including n, and removing that number \
    and its multiples from the set. The player that cannot make a move loses \
    the game. They play x rounds of the game, where n may be different for \
    each round. Assuming Maria always goes first and both players play \
    optimally, determine who the winner of each game is.

    Args:
        x (int): The number of rounds.
        nums (List[int]): An array of n.

    Returns:
        str: The name of the player that won the most rounds.
        If the winner cannot be determined, return `None`.
    """
    def is_prime(n):
        """
        Determines if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Generates a list of prime numbers up to n.

        Args:
            n (int): The upper limit of the range.

        Returns:
            List[int]: A list of prime numbers up to n.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def get_winner(primes, n):
        """
        Determines the winner of a game played with a set of prime numbers \
        up to n.

        Args:
            primes (List[int]): A list of prime numbers up to n.
            n (int): The upper limit of the range.

        Returns:
            str: The name of the player that won the game.
        """
        if not primes:
            return None
        if n in primes:
            return "Ben"
        if n - primes[-1] == 1:
            return "Ben"
        if primes[-1] == n - 2 and n > 2:
            return "Maria"
        for i in range(len(primes)):
            if i == len(primes) - 1:
                return "Ben"
            if primes[i] <= n - primes[i] <= primes[i + 1]:
                return "Ben"

    winners = {"Ben": 0, "Maria": 0}
    for n in nums:
        primes = get_primes(n)
        winner = get_winner(primes, n)
        if winner:
            winners[winner] += 1
    if winners["Ben"] > winners["Maria"]:
        return "Ben"
    elif winners["Maria"] > winners["Ben"]:
        return "Maria"
    else:
        return None


if __name__ == '__main__':
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
    print("Winner: {}".format(isWinner(3, [1, 1, 1])))
