from application.bases.base_mapper import BaseMapper
from api.representers.response.users.users import UserAuthorResponseRepresenter, UserProfileResponseRepresenter


class UserDTORepresenterMapper(BaseMapper):
    @staticmethod
    def user_dto__to__author(user_dto) -> UserAuthorResponseRepresenter:
        return UserAuthorResponseRepresenter(
            id=user_dto.id,
            username=user_dto.username
        )

    @staticmethod
    def user_profile_dto__to__user_profile(user_profile_dto) -> UserProfileResponseRepresenter:
        return UserProfileResponseRepresenter(
            username=user_profile_dto.username,
            name=user_profile_dto.name,
            email=user_profile_dto.email
        )
