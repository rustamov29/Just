def provision_server(clients_db, server_tiers, client_name, tier, months):
    if client_name not in clients_db:
        raise KeyError("Client unknown")

    if tier not in server_tiers:
        raise KeyError("Tier does not exist")

    if not isinstance(months, int) or months < 1:
        raise ValueError("Contract length invalid")

    total_cost = months * server_tiers[tier]["cost"]

    if months >= 12:
        total_cost -= server_tiers[tier]["discount"]

    if clients_db[client_name]["budget"] < total_cost:
        raise ValueError("Budget exceeded")

    clients_db[client_name]["budget"] -= total_cost
    return total_cost


def run_provisioning(clients_db, server_tiers, request_list):
    contract_value = 0.0
    errors_logged = 0

    for client, tier, months in request_list:
        try:
            contract_value += provision_server(
                clients_db, server_tiers, client, tier, months
            )
        except KeyError as e:
            print(f"Provisioning Failed: {e}")
            errors_logged += 1
        except ValueError as e:
            print(f"Provisioning Failed: {e}")
            errors_logged += 1

    return {
        "contract_value": contract_value,
        "errors_logged": errors_logged
    }

tiers = {
    "Basic": {"cost": 10.0, "discount": 10.0}, # Discount applies if 12+ months
    "Pro":   {"cost": 50.0, "discount": 50.0}
}

clients = {
    "StartupCo": {"budget": 200.0},
    "MegaCorp":  {"budget": 1000.0}
}

requests = [
    ("StartupCo", "Basic", 12),  # Valid. Cost: (12*10)-10 = 110. Rem: 90.
    ("StartupCo", "Pro", 5),     # Error: Cost 250 > 90.
    ("MegaCorp", "Ultra", 1),    # Error: Tier does not exist.
    ("GhostLLC", "Basic", 1),    # Error: Client unknown.
    ("MegaCorp", "Pro", 0.5)     # Error: Contract length invalid (type/value).
]

result = run_provisioning(clients, tiers, requests)

print(result)
