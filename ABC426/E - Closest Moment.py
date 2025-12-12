
import math

# 内積
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

# ベクトルの和
def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

# ベクトルの差
def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

# スカラー倍
def mul(a, s):
    return (a[0]*s, a[1]*s)

# ノルムの二乗（距離^2）
def norm2(a):
    return a[0]*a[0] + a[1]*a[1]

# p→q の長さと、単位方向ベクトル（q-p を正規化）を返す
def len_and_dir(p, q):
    vx, vy = q[0]-p[0], q[1]-p[1]
    L = math.hypot(vx, vy)      # = sqrt(vx^2 + vy^2)
    return L, (vx/L, vy/L)

# f(u) = ||d0 + w*u||^2 の最小値（二乗距離）を [0, delta] 上で求める
def min_quad_on_interval(d0, w, delta):
    # 左端 u=0
    best = norm2(d0)

    # 区間が空（delta<=0）なら左端のみ
    if delta <= 0:
        return best

    # 二次の係数 w^2 = ||w||^2
    w2 = dot(w, w)

    # 頂点候補 u_star（w2>0 のときのみ意味がある＝相対速度がゼロでない）
    if w2 > 0.0:
        u_star = - dot(d0, w) / w2
        # 頂点が区間 (0, delta) に入っていれば評価
        if 0.0 < u_star < delta:
            val_star = norm2(add(d0, mul(w, u_star)))
            if val_star < best:
                best = val_star

    # 右端 u=delta も評価
    valR = norm2(add(d0, mul(w, delta)))
    if valR < best:
        best = valR

    return best


def solve():
    T = int(input())
    out = []
    for _ in range(T):
        TSX, TSY, TGX, TGY = map(int, input().split())  # 高橋くん：スタートTS→ゴールTG
        ASX, ASY, AGX, AGY = map(int, input().split())  # 青木くん：スタートAS→ゴールAG

        TS = (float(TSX), float(TSY))
        TG = (float(TGX), float(TGY))
        AS = (float(ASX), float(ASY))
        AG = (float(AGX), float(AGY))

        # 各自の移動時間（速さ1なので距離=時間）と、単位方向ベクトル
        TT, vT = len_and_dir(TS, TG)  # 高橋くんの移動時間TTと進行方向vT
        TA, vA = len_and_dir(AS, AG)  # 青木くんの移動時間TAと進行方向vA

        # どちらが先に到着するかで時間区間を分ける
        t1 = min(TT, TA)  # 両者が同時に動く区間の終了時刻
        t2 = max(TT, TA)  # 片方のみ動く区間の終了時刻（=両者停止開始時刻）

        # 区間1：両者が動く [0, t1]
        # 相対位置 D(t) = (TS - AS) + (vT - vA)*t
        d0_1 = sub(TS, AS)      # 初期の差 TS - AS
        w_1  = sub(vT, vA)      # 相対速度 vT - vA
        ans2 = min_quad_on_interval(d0_1, w_1, t1)

        # 区間2：片方だけ動く [t1, t2]
        if TT < TA:
            # 高橋くんが先に到着 → 高橋くん停止、青木くんだけ動く
            AT_t1 = add(AS, mul(vA, t1))  # t1時点の青木くんの位置
            d0_2 = sub(TG, AT_t1)         # t1での差（高橋くんはTGで停止）
            w_2  = mul(vA, -1.0)          # 相対速度（高橋くん停止 - 青木くん）
            ans2 = min(ans2, min_quad_on_interval(d0_2, w_2, TA - TT))
        elif TA < TT:
            # 青木くんが先に到着 → 青木くん停止、高橋くんだけ動く
            TT_t1 = add(TS, mul(vT, t1))  # t1時点の高橋くんの位置
            d0_2 = sub(TT_t1, AG)         # t1での差（青木くんはAGで停止）
            w_2  = vT                     # 相対速度（高橋くん - 青木くん停止）
            ans2 = min(ans2, min_quad_on_interval(d0_2, w_2, TT - TA))
        # 同着（TT==TA）の場合、区間2は存在しない

        # 区間3：両方停止後（以降ずっと一定）
        ans2 = min(ans2, norm2(sub(TG, AG)))  # |TG - AG|^2

        # 最小距離（距離^2→平方根）を出力
        out.append(f"{math.sqrt(ans2):.10f}")

    print("\n".join(out))


if __name__ == "__main__":
    solve()