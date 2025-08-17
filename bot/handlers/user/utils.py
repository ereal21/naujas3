import html

from bot.localization import t
from bot.database.methods import (
    get_subcategories,
    get_all_items,
    get_item_info,
    select_item_values_amount,
    check_value,
)
from bot.misc import TgConfig


def build_menu_text(user_obj, balance: float, purchases: int, lang: str) -> str:
    """Return main menu text. Greeting remains in English regardless of language."""
    mention = f"<a href='tg://user?id={user_obj.id}'>{html.escape(user_obj.full_name)}</a>"
    basket_count = len(TgConfig.BASKETS.get(user_obj.id, []))
    return (
        f"{t(lang, 'hello', user=mention)}\n"
        f"{t(lang, 'balance', balance=f'{balance:.2f}')}\n"
        f"{t(lang, 'basket', items=basket_count)}\n"
        f"{t(lang, 'total_purchases', count=purchases)}\n\n"
        f"{t(lang, 'note')}"
    )


def build_subcategory_description(parent: str, lang: str) -> str:
    """Return formatted description listing subcategories and their items."""
    lines = [f" {parent}", ""]
    for sub in get_subcategories(parent):
        lines.append(f"🏘️ {sub}:")
        goods = get_all_items(sub)
        for item in goods:
            info = get_item_info(item)
            amount = select_item_values_amount(item) if not check_value(item) else '∞'
            lines.append(f"    • {item} ({info['price']:.2f}€) - {amount}")
        lines.append("")
    lines.append(t(lang, 'choose_subcategory'))
    return "\n".join(lines)


def blackjack_hand_value(cards: list[int]) -> int:
    total = sum(cards)
    aces = cards.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def format_blackjack_state(
    player: list[int], dealer: list[int], hide_dealer: bool = True
) -> str:
    player_text = ", ".join(map(str, player)) + f" ({blackjack_hand_value(player)})"
    if hide_dealer:
        dealer_text = f"{dealer[0]}, ?"
    else:
        dealer_text = ", ".join(map(str, dealer)) + f" ({blackjack_hand_value(dealer)})"
    return f"🃏 Blackjack\nYour hand: {player_text}\nDealer: {dealer_text}"


def get_blackjack_stats(user_id: int) -> dict:
    return TgConfig.STATE.setdefault(
        f"{user_id}_bj_stats", {"wins": 0, "losses": 0, "games": 0, "profit": 0.0}
    )


def blackjack_stats_text(stats: dict) -> str:
    games = stats["games"]
    win_rate = (stats["wins"] / games * 100) if games else 0
    return (
        f"🃏 Blackjack\nPNL: {stats['profit']:.2f}€\n"
        f"Win rate: {win_rate:.0f}% ({stats['wins']}/{games})\n\nSelect your bet:"
    )
