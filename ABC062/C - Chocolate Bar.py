h, w = map(int, input().split())

area = h * w

x_cut, y_cut = 0, 0
x_cut = int(round(w / 3))
y_cut = int(round(h / 3))

#You basically get 4 cases

x_rem = w - x_cut
y_rem = h - y_cut

x1_rem = x_rem // 2
y1_rem = h // 2

x2_rem = w // 2
y2_rem = y_rem // 2

case1 = [x_cut * h, x1_rem * h, (x_rem - x1_rem) * h]
case2 = [x_cut * h, y1_rem * x_rem, (h - y1_rem) * x_rem]
case3 = [y_cut * w, x2_rem * y_rem, (w - x2_rem) * y_rem]
case4 = [y_cut * w, y2_rem * w, (y_rem - y2_rem) * w]
cases = [case1, case2, case3, case4]

ans = 10 ** 9
for case in cases:
    ans = min(ans, max(case) - min(case))
print(ans)