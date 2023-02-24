from randStr import randWord, strMixer, randIntForWord

""""Testing for randStr. Not going to add additional comments to this but each function within randstr uses (word,
 i=None). i=None is an optional parameter and word is needed. Sometimes word must be 1 word."""


def main():
    print(randWord('The cow jumped over the moon'))
    print(randWord('The cow jumped over the moon'))
    print(randWord('The cow jumped over the moon'))
    print(randWord('The cow jumped over the moon'))
    print(randWord('The cow jumped over the moon', 4))
    print(randWord('The cow jumped over the moon', 4))
    print(randWord('The cow jumped over the moon', 4))
    print(randWord('The cow jumped over the moon', 4))
    print(randWord('The cow jumped over the moon', '4'))
    print(strMixer('The cow jumped over the moon'))
    print(strMixer('The cow jumped over the moon'))
    print(strMixer('The cow jumped over the moon'))
    print(strMixer('jumped'))
    print(strMixer('jumped'))
    print(strMixer('The cow jumped over the moon', 7))
    print(strMixer('The cow jumped over the moon', 7))
    print(strMixer('The cow jumped over the moon', 7))
    print(strMixer('jumped', 7))
    print(strMixer('jumped', '7'))
    print(randIntForWord('The cow jumped over the moon'))
    print(randIntForWord('jumped'))
    print(randIntForWord('jumped'))
    print(randIntForWord('jumped'))
    print(randIntForWord('jumped'))
    print(randIntForWord('The cow jumped over the moon', 9))
    print(randIntForWord('jumped', 9))
    print(randIntForWord('jumped', 9))
    print(randIntForWord('jumped', 9))
    print(randIntForWord('jumped', '9'))


main()  # executes main


