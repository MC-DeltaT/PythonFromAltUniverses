@spec get_data() :: {:ok, Data.t()} | {:error, term()}
def get_data() do
  with {:ok, response} <-
          HTTPoison.get(fiora_data_url(), [], timeout: @query_timeout, recv_timeout: @query_timeout),
        {:ok, body} <- handle_response(response),
        {:ok, json} <- Jason.decode(body),
        {:ok, data} <- json_to_data(json) do
    {:ok, data}
  else
    {:error, reason} -> {:error, reason}
  end
end
