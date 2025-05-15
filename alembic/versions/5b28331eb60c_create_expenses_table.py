"""Create expenses table

Revision ID: 5b28331eb60c
Revises: 
Create Date: 2025-04-10 15:20:25.906226

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func



# revision identifiers, used by Alembic.
revision: str = '5b28331eb60c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'expenses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('category', sa.String(255), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('expenses')
