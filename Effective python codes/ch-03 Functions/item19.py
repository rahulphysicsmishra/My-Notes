 #For example, say that I’m trying to determine various statistics for a population of
# alligators. Given a list of lengths, I need to calculate the minimum
#and maximum lengths in the population. Here, I do this in a single
# function that appears to return two values:


def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
print(sum(lengths), sorted(lengths))
minimum, maximum = get_stats(lengths)
print(f"Min: {minimum}, Max: {maximum}")

 #say I need another function that calculate how big each alligator is
 # relative to the population average. This function returns a list of ratios,
 # but I can receive the longest and shortest items individually by using a
 # starred expression for the middle portion of the list:

def get_avg_ratios(numbers):
    average = sum(numbers)/len(numbers)
    scaled = [x/average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *avg, shortest = get_avg_ratios(lengths)
print(f'long: {longest:>4.0%},short: {shortest:>4.0%}')

#  imagine that the program’s requirements change, and I need to
 # also determine the average length, median length, and total population
 # size of the alligators.

def stats(numbers):
    minimum1 = min(numbers)
    maximum1 = max(numbers)
    count = len(numbers)
    average1 = sum(numbers)/count
    sorted_list = sorted(numbers)
    middle = count//2
    if count % 2 == 0:
        lower = sorted_list[middle-1]
        upper = sorted_list[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_list[middle]
    return minimum1, maximum1, count, median, average1

min, max, count, median, average1 = stats(lengths)
print(f'min: {min}, max: {max}, count: {count}, median: {median}, avg: {average1}')