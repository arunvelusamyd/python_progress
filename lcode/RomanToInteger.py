class RomanToInteger:
    def convertRomanToInteger_1(ipStr: str) -> int:
        romanIntDict = {"I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000
                    }
        result = 0
        for number in range(len(ipStr)):
            if number < len(ipStr)-1 and romanIntDict.get(ipStr[number])<romanIntDict.get(ipStr[number+1]):
                result -= romanIntDict.get(ipStr[number])
            else:
                result += romanIntDict.get(ipStr[number])
        return result
