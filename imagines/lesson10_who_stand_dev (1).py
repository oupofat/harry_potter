class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

#UK Ratings are in the millions.
#These are my top 10 episodes (roughly)

DoctorWho = [
    Record(episode = "Eleventh Hour", season = 5, uk_ratings = 10.9, doctor = 11, writer = "moffat"),
    Record(episode = "Blink", season = 3, uk_ratings = 6.62, doctor = 10, writer = "moffat"),
    Record(episode = "Human Nature", season = 3, uk_ratings = 7.74, doctor = 10, writer = "cornell"),
    Record(episode = "Family of Blood", season = 3, uk_ratings = 7.21, doctor = 10, writer = "cornell"),
    Record(episode = "Silence in the Library", season = 4, uk_ratings = 6.27, doctor = 10, writer = "moffat"),
    Record(episode = "Forest of the Dead", season = 4, uk_ratings = 7.84, doctor = 10, writer = "moffat"),
    Record(episode = "Midnight", season = 4, uk_ratings = 8.05, doctor = 10, writer = "davies"),
    Record(episode = "A Good Man Goes to War", season = 6, uk_ratings = 7.51, doctor = 11, writer = "moffat"),
    Record(episode = "Let's Kill Hitler", season = 6, uk_ratings = 8.10, doctor = 11, writer = "moffat"),
    Record(episode = "Husbands of River Song", season = 9, uk_ratings = 7.69, doctor = 12, writer = "moffat")
]

#4 - What is the average and standard dev of the ratngs
import math

def mean_rating(DoctorWho):
    total_ratings = 0
    number_of_episodes = 0
    mean_ratings = 0
    for record in DoctorWho:
        total_ratings = total_ratings + record.uk_ratings
        number_of_episodes += 1
    mean_ratings = total_ratings / number_of_episodes
    return (mean_ratings)

def standard_deviation(DoctorWho):
    find_mean_ratings = mean_rating(DoctorWho)
    number_of_episodes = 0
    total_sum = 0
    for record in DoctorWho:
        number_of_episodes += 1
        total_sum += (record.uk_ratings - find_mean_ratings) ** 2
    standard_deviation = total_sum / number_of_episodes
    return math.sqrt(standard_deviation)


find_standard_deviation = standard_deviation(DoctorWho)
print ("The average ratings for the Doctor Who episodes is ", find_mean_ratings, "in the millions. The standard deviation of the average ratings is ", find_standard_deviation,".")

