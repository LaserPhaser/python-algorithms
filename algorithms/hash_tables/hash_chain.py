"""
A hash chain is the successive application of a cryptographic hash function to a piece of data.
In computer security, a hash chain is a method to produce many one-time keys from a single key or password. [Wikipedia]
"""


class HashChain(object):
    """
    Class HashChain realisation

    Examples:
        >>> hash_chain = HashChain(5)
        >>> hash_chain.add("world")
        >>> hash_chain.add("HellO")
        >>> hash_chain.check(4)
        HellO world
        >>> hash_chain.find("World")
        no
        >>> hash_chain.find("world")
        yes
        >>> hash_chain.delete("world")
        >>> hash_chain.check(4)
        HellO
        >>> hash_chain.delete("HellO")
        >>> hash_chain.add("luck")
        >>> hash_chain.add("GooD")
        >>> hash_chain.check(2)
        GooD luck


    Explanation:
    The ASCII code of ’w’ is 119, for ’o’ it is 111, for ’r’ it is 114,
    for ’l’ it is 108, and for ’d’ it is 100. Thus, h("world") = 4.
    It turns out that the hash value of “HellO“ is also 4.
    We always insert in the beginning of the chain, so after adding
    “world” and then “HellO” in the same chain index 4, first goes
    “HellO” and then goes “world”. Of course, “World” is not found,
    and “world” is found, because the strings are case-sensitive,
    and the codes of ’W’ and ’w’ are different. After deleting “world”,
    only “HellO” is found in the chain 4.
    Similarly to “world” and “HellO”, after adding “luck” and
    “GooD” to the same chain 2, first goes “GooD” and then “luck”.

    """

    def __init__(self, bucket_count):
        """

        Args:
            bucket_count: max count of hash chain
        """

        self._multiplier = 263
        self._prime = 1000000007
        self.bucket_count = bucket_count
        self.elements = [[] for _ in range(0, bucket_count)]

    def _hash_func(self, data):
        """
        Hash function
        Args:
            data: text for hashing

        Returns:
            result of hash function

        """

        ans = 0
        for c in reversed(data):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    @staticmethod
    def _form_chain(chain):
        """
        Function for formin chain

        Args:
            chain: text chain

        """
        return ' '.join(chain)

    def _check_data(self, data):
        """
        Function for check data in hash table

        Args:
            data: string data

        Returns:
            return hash string and data

        """
        hash_string = self._hash_func(data)
        try:
            ind = self.elements[hash_string].index(data)
        except ValueError:
            ind = -1
        return hash_string, ind

    def add(self, data):
        """
        Add data to hash table

        Args:
            data: string data
        """
        hash_string, ind = self._check_data(data)
        if ind == -1:
            self.elements[hash_string].append(data)

    def find(self, data):
        """
        Find data in hash table

        Args:
            data: string data

        Returns:
            True if found, False if not
        """
        _, ind = self._check_data(data)

        return ind != -1

    def delete(self, data):
        """
        Delete data from hash table

        Args:
            data: string data

        """
        hash_string, ind = self._check_data(data)
        if ind != -1:
            self.elements[hash_string].pop(ind)

    def check(self, idx):
        """
        Check hash_chain by index

        Args:
            idx: index in hash

        Returns:
            String chain separated by space
        """
        return self._form_chain(cur for cur in reversed(self.elements[idx]) if self._hash_func(cur) == idx)
