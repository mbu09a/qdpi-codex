// @ts-check
import js from '@eslint/js';
import tsParser from '@typescript-eslint/parser';

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
  js.configs.recommended,
  {
    files: ['**/*.ts', '**/*.tsx'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
      },
      globals: {
        __dirname: 'readonly',
        console: 'readonly',
      },
    },
    rules: {
      'no-unused-vars': [
        'error',
        { argsIgnorePattern: '^_' }
      ],
    },
  },
  {
    ignores: ['node_modules/', 'dist/'],
  },
  {
    languageOptions: {
      ecmaVersion: 2023,
      sourceType: 'module',
    },
  },
]; 