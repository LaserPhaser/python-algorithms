from algorithms.hash_tables.hash_chain import HashChain


class TestHashChain:
    def test_add(self):
        hash_chain = HashChain(5)
        hash_chain.add("world")
        hash_chain.add("HellO")
        res = hash_chain.check(4)
        assert 'HellO world' == res

    def test_find_no(self):
        hash_chain = HashChain(5)
        hash_chain.add("world")
        hash_chain.add("HellO")
        no = hash_chain.find("World")
        assert False is no

    def test_find_yes(self):
        hash_chain = HashChain(5)
        hash_chain.add("world")
        hash_chain.add("HellO")
        yes = hash_chain.find("world")
        assert True is yes

    def test_delete(self):
        hash_chain = HashChain(5)
        hash_chain.add("world")
        hash_chain.add("HellO")
        hash_chain.delete("world")
        res = hash_chain.check(4)
        assert 'HellO' == res
