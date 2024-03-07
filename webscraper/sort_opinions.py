def sort(opinions, sort_by):
    if sort_by == "highest":
        return opinions.sort(key=lambda opinion: opinion.stars, reverse=True)
    elif sort_by == "lowest":
        return opinions.sort(key=lambda opinion: opinion.stars)
    else:
        return opinions