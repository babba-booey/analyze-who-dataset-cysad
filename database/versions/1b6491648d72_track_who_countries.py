"""track who countries

Revision ID: 1b6491648d72
Revises: 8bb37ee1e037
Create Date: 2020-05-02 00:30:46.213517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b6491648d72'
down_revision = '8bb37ee1e037'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        create table who_countries(
            sequence_id text primary key,
            country_code text,
            country_name text,
            LAND_AREA_KMSQ_2012 float,
            MORT float,
            WHO_REGION text,
            WHO_REGION_CODE text,
            WORLD_BANK_INCOME_GROUP text,
            WORLD_BANK_INCOME_GROUP_CODE text,
            WORLD_BANK_INCOME_GROUP_GNI_REFERENCE_YEAR text
        )
        """
    )


def downgrade():
    op.execute(
        """
        drop table if exists
        who_countries
        cascade;
        """
    )
