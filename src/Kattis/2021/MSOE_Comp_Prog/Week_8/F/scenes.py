# Inspired by https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/dp/examples/scenes/Scenes.java#L56

def find_scenes(n, w, h, dp, mod):
    ribbon_squares = min(w * h, n)
    plains = ribbon_squares // w + 1

    return (find_scenes_recursive(1, w, ribbon_squares, dp, mod) - plains) % mod


def find_scenes_recursive(current_w, w, current_ribbon_squares, dp, mod):
    if current_ribbon_squares < 0:
        return 0
    elif current_w > w:
        return 1
    elif dp[current_w][current_ribbon_squares] != 0:
        return dp[current_w][current_ribbon_squares]
    else:
        scenes = 0

        for i in range(h + 1):
            scenes += find_scenes_recursive(current_w + 1, w, current_ribbon_squares - i, dp, mod)

        dp[current_w][current_ribbon_squares] = scenes % mod

        return scenes % mod


mod = int(1E9 + 7)
params = input().split(" ")
params = [int(param) for param in params]
n = params[0]
w = params[1]
h = params[2]
dp = [[0 for _ in range(n + 1)] for _ in range(w + 1)]

print(int(find_scenes(n, w, h, dp, mod)))
