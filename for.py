"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def CountMeanScore(scores):
    summ_of_scores = 0
    for score in scores:
        summ_of_scores += score
    mean_score = summ_of_scores / len(scores)
    map_of_scores = {"mean_score": mean_score, "total_score": summ_of_scores, "ammount_of_scores": len(scores)}
    return map_of_scores

def main():

    school = [
        {"school_class": "1a", "scores": [5, 5, 4, 5, 5]},
        {"school_class": "2a", "scores": [3, 4, 4, 5, 5]},
        {"school_class": "3a", "scores": [3, 4, 4, 5, 3]},
        {"school_class": "4a", "scores": [3, 4, 4, 5, 2]}
    ]

    overall_score = 0
    overall_ammount_of_scores = 0
    for school_class in school:
        map_for_class = CountMeanScore(school_class["scores"])
        overall_score += map_for_class["total_score"]
        overall_ammount_of_scores += map_for_class["ammount_of_scores"]
        print(f"Mean score for {school_class['school_class']} is {map_for_class['mean_score']}")
    overall_mean_score = overall_score / overall_ammount_of_scores
    print(f"Overall mean score is {overall_mean_score}")
    
if __name__ == "__main__":
    main()
