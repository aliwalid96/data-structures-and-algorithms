from hashtable import __version__
from hashtable.hashtable import hash_table

def test_version():
    assert __version__ == '0.1.0'
      
def test_set_data():
    new_hash = hash_table(2)
    new_hash.set('one', 1)
    new_hash.set('two', 2)
    new_hash.set('three', 3)
    new_hash.set('four', 4)
    new_hash.set('five', 5)
    print(new_hash)
    assert {'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}
