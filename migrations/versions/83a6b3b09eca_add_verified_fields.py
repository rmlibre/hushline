"""add verified fields

Revision ID: 83a6b3b09eca
Revises: 166a3402c391
Create Date: 2024-08-28 11:14:27.902082

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "83a6b3b09eca"
down_revision = "166a3402c391"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("extra_field_verified1", sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column("extra_field_verified2", sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column("extra_field_verified3", sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column("extra_field_verified4", sa.Boolean(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("extra_field_verified4")
        batch_op.drop_column("extra_field_verified3")
        batch_op.drop_column("extra_field_verified2")
        batch_op.drop_column("extra_field_verified1")
