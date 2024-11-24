# Victor Alcantara Menezes Mota GRR20230939
class VotingSystem:
    def __init__(self):
        self.voters = {}
        self.votes = {}

    def vote(self, voter_id, candidate):
        if voter_id in self.voters:
            return "Erro: Eleitor já votou."
        self.voters[voter_id] = True
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            self.votes[candidate] = 1
        return f"Voto registrado para {candidate}!"

    def show_results(self):
        results = []
        for candidate, count in self.votes.items():
            results.append(f"{candidate}: {count} votos")
        return "\n".join(results)


voting_system = VotingSystem()
print(voting_system.vote("123", "Alice"))
print(voting_system.vote("123", "Bob"))
print(voting_system.show_results())
