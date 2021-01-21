from sklearn.utils import check_random_state
random_state = check_random_state(14)
letters = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
shear_values = np.arange(0, 0.5, 0.05)


def generate_sample(random_state=None):
    random_state=check_random_state(random_state)
    letter = random_state.choice(letters)
    shear = random_state.choice(shear_values)


    return create_captcha(letter, shear=shear, size=(20,20)),letter.index(letter)


