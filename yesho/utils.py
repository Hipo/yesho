def get_model_properties(model, excluded_properties):
    """
    Returns the property names of the given model
    """
    # Get the field names
    field_list = model._meta.get_all_field_names()

    # Get the list of the attributes that are not fields.
    name_list = sorted([name for name in dir(model) if name not in field_list])

    property_list = list()
    # List only properties.
    for name in name_list:
        # If this property is excluded, do not even try to control it.
        if name in excluded_properties:
            continue
        if isinstance(getattr(model, name), property):
            property_list.append(name)
    return property_list
