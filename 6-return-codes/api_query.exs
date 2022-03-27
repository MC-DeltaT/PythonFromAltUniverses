defmodule HTTPError do
  @enforce_keys [:status_code, :message]
  defstruct
    status_code: 200,
    message: "OK"

  @type t() :: %__MODULE__{
    status_code: non_neg_integer(),
    message: String.t()
  }
end

defimpl String.Chars, for: HTTPError do
  def to_string(%HTTPError{status_code: code, message: message}) do
    "HTTP #{code} #{message}"
  end
end


@type api_data() :: String.t()


@spec api_query() :: {:ok, api_data()} | {:error, :timeout | HTTPError.t()}
def api_query do
  ...
end


case api_query() do
  {:ok, data} ->
    IO.puts("Got API data: #{data}")
  {:error, :timeout} ->
    IO.puts("Network timeout, retrying...")
    ...
  {:error, %HTTPError{status_code: code}} ->
    IO.puts("Got HTTP error code #{code}")
end


case api_query() do
  {:ok, data} ->
    IO.puts("Got API data: #{data}")
  {:error, reason} ->
    IO.puts("Failed to query API: #{reason}")
end
