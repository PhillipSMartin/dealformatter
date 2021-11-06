"""Classes encapsulating data used by dealviewer"""


class Constants:
    """Constants - various language-dependent constants used by multiple classes
    
        HONORS - one-character representations for ace through ten
        SUITS - one-character representations for spades, hearts, diamonds, and clubs
    """
    HONORS = 'AKQJT'
    SUITS = 'SHDC'


class SuitHolding:
    """One hand's holding in a single suit

    Constructor exceptions:
        ValueError - invalid input

    Format specifications:
        NULL -  for console display
        h -     formatted for html
    """

    SUIT_PIPS = '\u2660\u2661\u2662\u2663'
    SUIT_PIPS_HTML = ['&#9824;', 
        '<span style="color: rgb(192, 22, 22);">&#9829;</span>', 
        '<span style="color: rgb(192, 22, 22);">&#9830;</span>', 
        '&#9827;']

    def __init__(self, suit, cards):
        self._suit = self._validate_suit(suit)
        self._cards = self._validate_cards(cards)

    def _validate_suit(self, suit):
        try:
            suit = suit.upper()
            if suit not in Constants.SUITS:
                raise ValueError
            return suit

        except (ValueError, AttributeError):
            raise ValueError(f'Suit must be one of {Constants.SUITS}')

    def _validate_cards(self, cards):
        try:
            cards = cards.upper().replace('X','x')
            valid_cards = Constants.HONORS + '98765432x'

            last_index = -1
            for card in cards:
                current_index = valid_cards.index(card)
                if current_index < last_index \
                        or (current_index == last_index and card != 'x'):
                    raise ValueError
                last_index = current_index
            return cards

        except (ValueError, AttributeError):
            raise ValueError(f'Cards must consist of {Constants.HONORS}98765432 or x'
                ' in proper order')

    @property
    def suit(self):
        """one-character representation of suit (in English, S, H, D, or C)"""
        return self._suit

    @property
    def cards(self):
        """string containing one character for each card (T = 10)"""
        return self._cards

    @property
    def _suit_pip(self):
        return SuitHolding.SUIT_PIPS[Constants.SUITS.index(self.suit)]

    @property
    def _suit_pip_html(self):
        return SuitHolding.SUIT_PIPS_HTML[Constants.SUITS.index(self.suit)]

    def __repr__(self):
        return f"{type(self).__name__}(suit='{self.suit}', cards='{self.cards}')"

    def __str__(self):
        return format(self)

    def __format__(self, format_spec):
        if format_spec and format_spec in 'hH':
            pip = self._suit_pip_html
        else:
            pip = self._suit_pip
        return pip + ' ' + (' '.join(self.cards).replace('T', '10') or '--')


class Hand:
    """one hand's holdings in all four suits
 
    Constructor exceptions:
        ValueError - invalid input

    Format specifications:
        NULL -  for console display
        h -     formatted for html
    """

    def __init__(self, spades, hearts, diamonds, clubs):
        self._spades = SuitHolding(Constants.SUITS[0], spades)
        self._hearts = SuitHolding(Constants.SUITS[1], hearts)
        self._diamonds = SuitHolding(Constants.SUITS[2], diamonds)
        self._clubs = SuitHolding(Constants.SUITS[3], clubs)

    @property
    def spades(self):
        """ holding in spades, represented as a string containing one character 
            for each card (t = 10)
        """
        return self._spades.cards

    @property
    def hearts(self):
        """ holding in hearts, represented as a string containing one character 
            for each card (t = 10)
        """
        return self._hearts.cards

    @property
    def diamonds(self):
        """ holding in diamonds, represented as a string containing one character 
            for each card (t = 10)
        """
        return self._diamonds.cards

    @property
    def clubs(self):
        """ holding in clubs, represented as a string containing one character 
            for each card (t = 10)
        """
        return self._clubs.cards

    @property
    def _suits(self):
        return [self._spades, self._hearts, self._diamonds, self._clubs]

    def __repr__(self):
        return (f"{type(self).__name__}(spades='{self.spades}', " 
            f"hearts='{self.hearts}', "
            f"diamonds='{self.diamonds}', "
            f"clubs='{self.clubs}')")

    def __str__(self):
        return format(self)

    def __format__(self, format_spec):
        if format_spec and format_spec in 'Hh':
            joiner = '&nbsp;&nbsp;'
        else:
            joiner = '  '
        return joiner.join(format(suit, format_spec) for suit in self._suits)


if __name__ == '__main__':
    h = Hand('ajt8', 'aqt432', 'a5', '7')
    print(f'{h!r}')
    print(f'{h:h}')
    print(h)
    

    