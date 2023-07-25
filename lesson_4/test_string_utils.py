import pytest
from string_utils import StringUtils

stringutils = StringUtils()

@pytest.mark.positive_test  
def test_string_positive():
    stringutils = StringUtils()
    res = stringutils.capitilize("skypro")
    assert res == 'Skypro' 

@pytest.mark.positive_test  
def test_trim_positive():
    stringutils = StringUtils()
    res = stringutils.trim(" 04 апреля 2023")
    assert res == '04 апреля 2023' 

@pytest.mark.positive_test  
def test_to_list_positive_1():
    stringutils = StringUtils()
    res = stringutils.to_list("123456")
    assert res == ["123456"]

@pytest.mark.positive_test  
def test_to_list_positive_2():
    stringutils = StringUtils()
    res = stringutils.to_list("1:2:3", ":")
    assert res == ["1", "2", "3"]

@pytest.mark.positive_test  
def test_contains_positive_1():
    stringutils = StringUtils()
    if stringutils.contains("Тест", "е"):
        res = True
        assert res == True    

@pytest.mark.positive_test  
def test_contains_positive_2():
    stringutils = StringUtils()
    if stringutils.contains("SkyPro", "U"):
        res = False
        assert res == False

@pytest.mark.positive_test  
def test_delete_symbol_positive_1():
    stringutils = StringUtils()
    res = stringutils.delete_symbol("Тест", "е")
    assert res == "Тст"

@pytest.mark.positive_test  
def test_delete_symbol_positive_2():
    stringutils = StringUtils()
    res = stringutils.delete_symbol("SkyPro", "o")
    assert res == "SkyPr"

@pytest.mark.positive_test    
def test_starts_with_positive_1():
    stringutils = StringUtils()
    if stringutils.starts_with("Тест", "Т"):
        res = True
        assert res == True 
    else:
        res = False
        assert res == False

@pytest.mark.positive_test   
def test_end_with_positive_1():
    stringutils = StringUtils()
    res = stringutils.end_with("SkyPro", "o")
    assert res == True 
   
@pytest.mark.positive_test   
def test_end_with_positive_2():
    stringutils = StringUtils()
    res = stringutils.end_with("SkyPro", "k")
    assert res == False

@pytest.mark.positive_test  
def test_list_to_string_positive_1():
    stringutils = StringUtils()
    res = stringutils.list_to_string(["Тест", "123", "04 апреля 2023"])
    assert res == "Тест, 123, 04 апреля 2023"


@pytest.mark.negative_test  
def test_string():
    stringutils = StringUtils()
    res = stringutils.capitilize("")
    assert res == '' 

@pytest.mark.negative_test  
def test_trim():
    stringutils = StringUtils()
    res = stringutils.trim("")
    assert res == '' 

@pytest.mark.negative_test  
def test_to_list():
    stringutils = StringUtils()
    res = stringutils.to_list("")
    assert res == []


@pytest.mark.negative_test  
def test_contains():
    stringutils = StringUtils()
    if stringutils.contains("Тест", "a"):
        res = False
        assert res == False    


@pytest.mark.negative_test  
def test_delete_symbol():
    stringutils = StringUtils()
    res = stringutils.delete_symbol("Тест", "a")
    assert res == "Тест"

@pytest.mark.negative_test    
def test_starts_with():
    stringutils = StringUtils()
    res = stringutils.starts_with("Тест", "Е")
    assert res == False


@pytest.mark.negative_test   
def test_end_with():
    stringutils = StringUtils()
    res = stringutils.end_with("Тест", "у")
    assert res == False 
   

@pytest.mark.negative_test  
def test_list_to_string():
    stringutils = StringUtils()
    res = stringutils.list_to_string([])
    assert res == ""

