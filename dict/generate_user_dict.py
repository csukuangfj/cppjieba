#!/usr/bin/env python3
from pypinyin import phrases_dict


def main():
    phrases = phrases_dict.phrases_dict

    with open("./user.dict.utf8", "w", encoding="utf-8") as f:
        for phrase in phrases:
            f.write(f"{phrase} 10000 v\n")


if __name__ == "__main__":
    main()
