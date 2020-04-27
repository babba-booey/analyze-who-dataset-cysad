"""create data sources

Revision ID: 8bb37ee1e037
Revises: 
Create Date: 2020-04-27 21:49:32.187963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bb37ee1e037'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        create table if not exists data_sources (
            data_source_id text primary key,
            data_source_name text
        );
        """
    )


def downgrade():
    op.execute(
        """
        drop table if exists data_sources;
        """
    )
