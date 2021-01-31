import re

def solution(files):
    return sorted(files,
        key=lambda x: (
            re.search(r"(\D+)(\d+)(.*)", x).group(1).lower(),
            int(re.search(r"(\D+)(\d+)(.*)", x).group(2))
        )
    )

if __name__ == '__main__':
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))