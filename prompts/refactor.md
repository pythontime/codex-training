Refactor the selected code following clean code principles and best practices.

## Analysis Phase
1. Identify code smells: long methods, deep nesting, duplicate code, magic numbers
2. Check for SOLID principle violations
3. Note any unclear naming or missing abstractions

## Refactoring Steps
1. **Extract Methods**: Break complex logic into small, focused functions (< 20 lines)
2. **Meaningful Names**: Use descriptive variable, function, and class names
3. **Remove Duplication**: Apply DRY principle, extract shared logic
4. **Simplify Conditionals**: Replace nested if/else with early returns or guard clauses
5. **Error Handling**: Add appropriate try/catch blocks and validation

## Code Quality
- Maintain consistent formatting and indentation
- Add comments only where intent isn't clear from code
- Ensure backward compatibility unless explicitly changing behavior
- Keep changes minimal and focused

## Output
- Show the refactored code with brief explanations of major changes
- Highlight any behavioral changes that need verification
- Suggest follow-up improvements if applicable
