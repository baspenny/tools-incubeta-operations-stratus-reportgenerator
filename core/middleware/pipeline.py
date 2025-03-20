from app.models import Profile


def update_user_social_data(strategy, *args, **kwargs):
    response = kwargs["response"]
    _backend = kwargs["backend"]
    user = kwargs["user"]

    if response.get("picture"):

        try:
            userProfile_obj = Profile.objects.get(user=user)
            print("Found existing profile, updating now")
        except Profile.DoesNotExist:
            print("No profile for user, creating one now")
            userProfile_obj = Profile()
            userProfile_obj.user = user

        userProfile_obj.user.last_name = response.get("given_name")
        userProfile_obj.user.first_name = response.get("family_name")
        userProfile_obj.picture = response.get("picture")
        userProfile_obj.save()