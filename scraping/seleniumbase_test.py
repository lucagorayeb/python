from seleniumbase import SB

with SB(uc=True, test=True, locale="en") as sb:
    url = "https://medium.com/codex/day-1-introduction-to-linux-5e7795be5d00"
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    sb.solve_captcha()