amend:
	git commit --amend --no-edit

release:
	@$(if $(strip $(VERSION)),:,$(error VERSION is required, e.g. make release VERSION=1.2.3))
	sed -i '' 's/^version = ".*"/version = "$(VERSION)"/' pyproject.toml
	git add pyproject.toml README*.md
	git commit -m "chore: bump version to $(VERSION)"
	git tag -a "v$(VERSION)" -m "v$(VERSION)"
	git push --tags
	git push
