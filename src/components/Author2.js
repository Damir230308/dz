import React from 'react';

const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.id}
            </td>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        ID
                    </th>
                </tr>
                <tr>
                    <th>
                        First name
                    </th>
                </tr>
                <tr>
                    <th>
                        Birthday year
                    </th>
                </tr>
                <tr>
                    {authors.map((author) => <AuthorItem author={author}/>)}
                </tr>
            </thead>
        </table>
    )
    }
export default AuthorList
