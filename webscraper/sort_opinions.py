import datetime

def sort(opinions, sort_by):
    if sort_by == "highest":
        return opinions.sort(key=lambda opinion: opinion.stars if opinion.stars is not None else 0, reverse=True)
    elif sort_by == "lowest":
        return opinions.sort(key=lambda opinion: opinion.stars if opinion.stars is not None else 0)
    elif sort_by == "recommend":
        return opinions.sort(key=lambda opinion: opinion.recommendation if opinion.recommendation is not None else '', reverse=True)
    elif sort_by == "not-recommend":
        return opinions.sort(key=lambda opinion: opinion.recommendation if opinion.recommendation is not None else '')
    elif sort_by == "vote-useful":
        return opinions.sort(key=lambda opinion: opinion.helpfull if opinion.helpfull is not None else 0, reverse=True)
    elif sort_by == "vote-not-useful":
        return opinions.sort(key=lambda opinion: opinion.not_helpfull if opinion.not_helpfull is not None else 0, reverse=True)
    elif sort_by == "verified":
        # verified first
        return opinions.sort(key=lambda opinion: opinion.confirmed_purchase, reverse=True)
    elif sort_by == "oldest":
        return opinions.sort(key=lambda opinion: opinion.date_of_opinion if opinion.date_of_opinion is not None else datetime.datetime.now())
    elif sort_by == "newest":
        return opinions.sort(key=lambda opinion: opinion.date_of_opinion if opinion.date_of_opinion is not None else datetime.datetime.now(), reverse=True)
    else:
        return opinions
    