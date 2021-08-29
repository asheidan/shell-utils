#!/bin/bash

set -e

input=${1:-'-'}

pandoc \
	--wrap=none \
	-f html \
	-t org \
	"${input}" \
	--lua-filter <( cat <<'EOLUA'
local function starts_with(start, str)
	return str:sub(1, start:len()) == start
end

return {
	{
		Div = function (elem)
			return elem.content
		end,

		Header = function (elem)
			-- Goal is to remove all properties from headers to remove the need for that drawer in org-mode

			-- Setting classes to empty list will remove the need for the CLASS property which is ugly
			elem.classes = {}

			-- Setting the identifier to an empty string removes the need of setting the property in org-mode
			-- Setting the identifier to nil removes the header alltogether
			elem.identifier = ""

			return elem
		end,

		Image = function (elem)
			if starts_with("data:", elem.src) then
				return {}
			end

			return nil
		end,

		Link = function (elem)
			if (starts_with("#", elem.target) and next(elem.content) == nil) then
				return {}
			end

			return nil
		end,

		SoftBreak = function (elem)
			return {}
		end,
	},
}
EOLUA
)
