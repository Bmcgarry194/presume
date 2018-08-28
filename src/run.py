"""Command line script for creating a profile
"""

from profile import Profile


def add_profile_CLI():
    # enter name
    name = input("Enter your name: ")
    new_profile = Profile(name)
    print(new_profile)

    # enter address
    # street = input("Enter your street: ")
    # city = input("Enter your city: ")
    # state = input("Enter your state (ex: WA): ")
    # zip = input("Enter your zip: ")
    #
    # new_profile.edit_address(street, city, state, zip)
    # print(new_profile)
    # print(new_profile.address)

    # enter skills
    skills = input("Enter your skills delimited by commas: ")
    skills = skills.split(',')
    skills = [skill.strip() for skill in skills]
    print(skills)
    new_profile.edit_skills(skills)
    # print(new_profile.skills)

    skills = input("Enter more skills: ")
    skills = skills.split(',')
    skills = [skill.strip() for skill in skills]
    print(skills)
    new_profile.edit_skills(skills)
    # print(new_profile.skills)


if __name__ == "__main__":
    # example = Profile(name="Tester McTasty", phone_num="8087654321",
    #                   email="mctasty@me.com")
    #
    # example.edit_address(street="775 McNeill St.")

    add_profile_CLI()
