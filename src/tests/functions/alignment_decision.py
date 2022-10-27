def alignment_decision():
    align = input('Are you Good, Evil, or Neutral?: ')
    if align.lower() == 'good':
        return('Good')
    elif align.lower() == 'evil':
        return('Evil')
    elif align.lower() == 'neutral':
        return('Neutral')
    else:
        print('You messed up'), alignment_decision()
        