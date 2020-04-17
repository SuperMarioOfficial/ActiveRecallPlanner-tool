from datetime import timedelta
from ics import Calendar, Event


def create_event(name, date):
    e = Event()
    e.name = name
    e.begin = date
    e.make_all_day()

    return e


def revision_block_plan(subject, block, date, delta):
    revision_one = date + timedelta(days=delta + 1)
    revision_two = date + timedelta(days=delta + 3)
    revision_three = date + timedelta(days=delta + 6)
    revision_four = date + timedelta(days=delta + 21)

    print("Revision schedule Subject[{subject}] week[{block}]:\n"
          "Starting to study on {today}\n"
          "revision one -> {revision_one}\n"
          "revision two -> {revision_two}\n"
          "revision three -> {revision_three}\n"
          "revision four -> {revision_four}\n".format(today=date + timedelta(days=delta), subject=subject + 1,
                                                      block=block + 1,
                                                      revision_one=revision_one,
                                                      revision_two=revision_two, revision_three=revision_three,
                                                      revision_four=revision_four)
          )


def create_study_plan():
    from datetime import date
    subjects = 1
    weeks = 12

    date = date.today()
    with open('recall_calendar.ics', 'w') as file:
        c = Calendar()
        for subject in range(subjects):
            for block in range(weeks):
                if block < 1:
                    revision_block_plan(subject, block, date, block + subject)
                    start = date + timedelta(days=block + subject + 0)
                    revision_one = date + timedelta(days=block + subject + 1)
                    revision_two = date + timedelta(days=block + subject + 3)
                    revision_three = date + timedelta(days=block + subject + 6)
                    revision_four = date + timedelta(days=block + subject + 21)

                    event0 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[0] date[{revision}]".format(subject=subject, block=block,
                                                                                    revision=start),
                        start)

                    event1 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[1] date[{revision}]".format(subject=subject, block=block,
                                                                                      revision=revision_one),
                        revision_one)

                    event2 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[2] date[{revision}]".format(subject=subject, block=block,
                                                                                      revision=revision_two),
                        revision_two)
                    event3 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[3] date[{revision}]".format(subject=subject, block=block,
                                                                                    revision=revision_three),
                        revision_three)
                    event4 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[4] date[{revision}]".format(subject=subject, block=block,
                                                                                    revision=revision_four),
                        revision_four)

                    c.events.add(event0)
                    c.events.add(event1)
                    c.events.add(event2)
                    c.events.add(event3)
                    c.events.add(event4)
                else:
                    revision_block_plan(subject, block, date, (6 * block) + subject)
                    start = date + timedelta(days=(6 * block) + subject + 0)
                    revision_one = date + timedelta(days=(6 * block) + subject + 1)
                    revision_two = date + timedelta(days=(6 * block) + subject + 3)
                    revision_three = date + timedelta(days=(6 * block) + subject + 6)
                    revision_four = date + timedelta(days=(6 * block) + subject + 21)

                    event0 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[0] date[{revision}]".format(subject=subject, block=block,
                                                                                 revision=start),
                        start)

                    event1 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[1] date[{revision}]".format(subject=subject, block=block,
                                                                                 revision=revision_one),
                        revision_one)

                    event2 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[2] date[{revision}]".format(subject=subject, block=block,
                                                                                 revision=revision_two),
                        revision_two)
                    event3 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[3] date[{revision}]".format(subject=subject, block=block,
                                                                                 revision=revision_three),
                        revision_three)
                    event4 = create_event(
                        "Revision subject[{subject}] week[{block}] revision[4] date[{revision}]".format(subject=subject, block=block,
                                                                                 revision=revision_four),
                        revision_four)

                    c.events.add(event0)
                    c.events.add(event1)
                    c.events.add(event2)
                    c.events.add(event3)
                    c.events.add(event4)
        file.writelines(c)
    file.close()


create_study_plan()
