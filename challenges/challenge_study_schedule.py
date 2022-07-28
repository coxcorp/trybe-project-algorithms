def study_schedule(permanence_period, target_time):
    try:
        quantity = 0
        for schedule in permanence_period:
            if schedule[0] <= target_time <= schedule[1]:
                quantity += 1
        return quantity

    except TypeError:
        return None
