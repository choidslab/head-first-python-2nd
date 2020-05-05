def search4vowels(phrase: str) -> set:  # Function Annotation 함수의 인자 유형 또는 리턴 유형을 문서화 하는 기능
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrases'."""
    return set(letters).intersection(set(phrase))
