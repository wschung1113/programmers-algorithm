def solution(cap, n, deliveries, pickups):
    ans = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    dcap, dix = 0, 0
    pcap, pix = 0, 0
    for ix in range(n):
        dcap += deliveries[ix]
        pcap += pickups[ix]
        while dcap > 0 or pcap > 0:
            dcap -= cap
            pcap -= cap
            ans += 2 * (n - ix)
    return ans