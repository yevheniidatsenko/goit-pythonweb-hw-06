import sys
import os
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

# Import your database configuration and models
from database_config import url_to_db  # Import the database URL from your config file
from db_engine.models import Base  # Import your SQLAlchemy Base for metadata

# Add the project root directory to sys.path for proper imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Alembic Config object, which provides access to .ini file values
config = context.config

# Set the SQLAlchemy URL dynamically from database_config.py
config.set_main_option("sqlalchemy.url", url_to_db)

# Configure logging for Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for autogenerate support (SQLAlchemy models)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL and not an Engine.
    Calls to context.execute() emit the given string to the script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario, we need to create an Engine and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Determine whether we are running in offline or online mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()