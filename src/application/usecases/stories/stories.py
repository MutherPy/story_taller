from application.bases.base_usecase import BaseUseCase


class CreateStory(BaseUseCase):
    async def __call__(self, author_id, title, text, tags_ids):
        try:
            await self.uow.db.story_c_rep.create_story(
                author_id=author_id,
                title=title,
                text=text,
                tags_ids=tags_ids
            )
            await self.uow.commit()
            return True
        except Exception:
            await self.uow.rollback()
            raise


class ListStoriesForUser(BaseUseCase):
    async def __call__(self, user_id, tags_ids):
        result = await self.uow.db.story_q_rep.get_user_stories(user_id=user_id, tags_ids=tags_ids)
        return result


class RetrieveStory(BaseUseCase):
    async def __call__(self, story_id):
        result = await self.uow.db.story_q_rep.get_story_by_id(story_id=story_id)
        return result
