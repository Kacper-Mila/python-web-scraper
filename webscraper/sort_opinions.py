def sort(opinions, sort_by):
    if sort_by == "highest":
        return opinions.sort(key=lambda opinion: opinion.stars if opinion.stars is not None else 0, reverse=True)
    elif sort_by == "lowest":
        return opinions.sort(key=lambda opinion: opinion.stars if opinion.stars is not None else 0)
    elif sort_by == "recommend":
        return opinions.sort(key=lambda opinion: opinion.recommendation if opinion.recommendation is not None else '', reverse=True)
    elif sort_by == "not-recommend":
        return opinions.sort(key=lambda opinion: opinion.recommendation if opinion.recommendation is not None else '')
    else:
        return opinions
    