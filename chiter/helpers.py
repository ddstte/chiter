def is_chiter(cls, f) -> bool:
    if not hasattr(f, "__annotations__"):
        return False

    return_type = f.__annotations__.get("return", "")
    parts = str(return_type).split(".")
    return any((p for p in parts if p.startswith(cls.__name__)))
